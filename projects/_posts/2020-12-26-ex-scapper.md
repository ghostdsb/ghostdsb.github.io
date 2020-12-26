---
layout: post
title:  "Ex Scapper"
date:   2020-12-26 13:28:13 +0530
category: Project
permalink: "projects/exscapper"
---

### Elixir module that looked for answered questions in a github [repo](https://github.com/ghostdsb/ProjectEuler) and scrapped project euler [site](https://projecteuler.net/archives) for their questions.

#### Fetching answers from Repository
---

First we hit github's content API to get all the files in the repo. For this, I used Elixir HTTPoison module.

```elixir
 def get_answer_list() do
    with {:ok, %HTTPoison.Response{status_code: 200, body: body}} <- HTTPoison.get("https://api.github.com/repos/ghostdsb/ProjectEuler/contents"),
    {:ok, data} <- Jason.decode(body) do
      data
      |> Enum.map(fn entry -> entry["name"] end)
      |> Enum.filter(fn x -> is_answer?(x) end)
    else
      _ -> "err"
    end
  end
```

This gives us a list of all the file names in the repo. Now for each file name we hit another github's API for getting file contents and some useful header details like last modified date

```elixir
def get_answer_data(file_name) do
    with {:ok, %HTTPoison.Response{status_code: 200, body: body, headers: headers}} <- HTTPoison.get("https://api.github.com/repos/ghostdsb/ProjectEuler/contents/"<>file_name<>"?ref=master") do
      {:ok, data} = body |> Jason.decode()
      data =
        data["content"]
        |> String.split("\n")
        |> Enum.map(fn line -> line |> Base.decode64!() end)
        |> Enum.join()
      file_name |> IO.inspect()
        %{
        "body" => data,
        "headers" => headers |> Map.new()
      }
    else
      _ ->
      %{
        "body" => "#error",
        "headers" => %{"last-modified" => "error"}
      }
    end
  end
```

#### Scrapping questions from Project Euler site
---

Same HTTPoison module is used to fetch the site details. But now another elixir module Floki which is a simple HTML parser that enables search for nodes using CSS selectors. Upon inspecting the site, it is found that the question title is wrapped in a "h2" tag and the question content is inside a div with class name "problem_content".

```elixir
def get_question(question_number) do
    with {:ok, %HTTPoison.Response{status_code: 200, body: body}} <- HTTPoison.get("https://projecteuler.net/problem=" <> question_number) do

      title = body
      |> Floki.find("h2")
      |> Enum.map(fn content -> htmlfy(content) end)
      |> List.first()

      question = body
      |> Floki.find("div.problem_content")
      |> Enum.map(fn content -> htmlfy(content) end)
      |> List.first()

      %{"title" => title,
      "content" => question}
    else
      _ -> %{"title" => "<h2>question-title</h2>", "content" => "<div>question-body</div>"}
    end
  end
```

The only issue is Floki returns HTML data as a tuple of {tag_name, attributes, children_nodes_list}

```elixir
iex> {:ok, %HTTPoison.Response{status_code: 200, body: body}} = HTTPoison.get("https://projecteuler.net/problem=001")
iex> body |> Floki.find("div.problem_content")
iex> [
    {"div", [{"class", "problem_content"}, {"role", "problem"}],
     [
       {"p", [],
        ["If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23."]},
       {"p", [], ["Find the sum of all the multiples of 3 or 5 below 1000."]}
     ]}
  ]
```

So a function htmlfy is used to make valid HTML page from this.

```elixir
def htmlfy({tag_name, _attributes, []}) do
    "<#{tag_name}/>"
end

def htmlfy({tag_name, _attributes, children_nodes}) do
    "<#{tag_name}>#{Enum.reduce(children_nodes,"",fn child, acc -> acc <> htmlfy(child) end )}</#{tag_name}>"
end

def htmlfy(string_child), do: string_child
```

Now we can get an HTML code
```elixir
iex> {:ok, %HTTPoison.Response{status_code: 200, body: body}} = HTTPoison.get("https://projecteuler.net/problem=001")
iex> body|> Floki.find("h2") |> Enum.map(fn content -> htmlfy(content) end) |> List.first()
iex> "<div><p>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.</p><p>Find the sum of all the multiples of 3 or 5 below 1000.</p></div>"
```

### Final Optimisation

Wrapped the building script in a Task to run the process of fetching each problems's question and answer asynchronously.
```elixir
  def fetch_data_from_gh(file_name) do
    Task.start(fn -> build_solution(file_name) end)
  end
```

[ExScapper's repo](https://github.com/ghostdsb/ex_scapper)