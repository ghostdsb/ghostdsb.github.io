---
layout: post
title:  "Ex Scaper"
date:   2020-12-26 13:28:13 +0530
category: Project
permalink: "projects/exscapper"
---

### Elixir module that looks for answered problems in my Project Euler [repo](https://github.com/ghostdsb/ProjectEuler) and scraped Project Euler [site](https://projecteuler.net/archives) for their questions.

#### This project is done to teach self about 

| - |
| Webscraping in Elixir|
| Github APIs.|

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
```elixir
iex(1)> ExScapper.get_answer_list
["pe001-multiple-of-3-and-5.py", "pe002-even-fibonacci-numbers.py",
 "pe003-largest-prime-factor.py", "pe004-largest-palindrome-product.py",
 "pe005-smallest-multiple.py", "pe006-sum-square-difference.py",
 "pe007-10001st-prime-number.py", "pe008-largest-product-in-a-series.py",
 "pe009-special-pythagorean-triplet.py", "pe010-summation-of-primes.py",
 "pe011-largest-product-in-a-grid.py",
 "pe012-highly-divisible-triangular-number.py", "pe013-large-sum.py",
 "pe014-longest-collatz-sequence.py", "pe015-lattice-path.py",
 "pe016-power-digit-sum.py", "pe017-number-letter-counts.py",
 "pe018-maximum-path-sum-I.py", "pe019-counting-sundays.py",
 "pe020-factorial-digit-sum.py", "pe021-amicable-numbers.py",
 "pe023-non-abundant-sums.py", "pe024-lexicographic-mutations.py",
 "pe025-1000-digit-fibonacci-number.py", "pe026-reciprocal-cycles.py",
 "pe027-quadratic-primes.py", "pe028-number-spiral-diagonals.py",
 "pe029-distinct-power.py", "pe030-digit-5th-power.py", "pe031-coin-sum.py",
 "pe032-pandigital-products.py", "pe033-digit-cancelling-fractions.py",
 "pe034-digit-factorials.py", "pe035-circular-primes.py",
 "pe036-double-base-palindrome.py", "pe037-truncatable-prime.py",
 "pe038-pandigital-multiples.py", "pe039-integer-right-triangles.py",
 "pe040-champernowne-constant.py", "pe041-pandigital-primes.py",
 "pe042-coded-triangle-number.py", "pe043-sub-string-divisibility.py",
 "pe044-pentagon-numbers.py", "pe045-triangular-pentagonal-hexagonal.py",
 "pe046-goldbach's-other-conjenture.py", "pe047-distinct-prime-factors.py",
 "pe048-self-power.py", "pe050-consecutive-prime-sum.py",
 "pe051-prime-digit-replacements(inc).py", "pe052-permuted-multiples.py", ...]
```
This gives us a list of all the file names in the repo. 
<br/>
<br/>
Now for each file name we hit another github's API for getting file contents and some useful header details like ```last-modified``` date.

```elixir
iex(2)> HTTPoison.get("https://api.github.com/repos/ghostdsb/ProjectEuler/contents/pe001-multiple-of-3-and-5.py?ref=master")
{:ok,
 %HTTPoison.Response{
   body: "{\"name\":\"pe001-multiple-of-3-and-5.py\",\"path\":\"pe001-multiple-of-3-and-5.py\",\"sha\":\"8f42d5105610d2625069cea1605ec833b0ba279a\",\"size\":79,\"url\":\"https://api.github.com/repos/ghostdsb/ProjectEuler/contents/pe001-multiple-of-3-and-5.py?ref=master\",\"html_url\":\"https://github.com/ghostdsb/ProjectEuler/blob/master/pe001-multiple-of-3-and-5.py\",\"git_url\":\"https://api.github.com/repos/ghostdsb/ProjectEuler/git/blobs/8f42d5105610d2625069cea1605ec833b0ba279a\",\"download_url\":\"https://raw.githubusercontent.com/ghostdsb/ProjectEuler/master/pe001-multiple-of-3-and-5.py\",\"type\":\"file\",\"content\":\"I3BlMDAxDQphcnIgPSBbeCBmb3IgeCBpbiByYW5nZSgxLDEwMDApIGlmIHgl\\nMz09MCBvciB4JTU9PTBdDQpwcmludChzdW0oYXJyKSkNCg==\\n\",\"encoding\":\"base64\",\"_links\":{\"self\":\"https://api.github.com/repos/ghostdsb/ProjectEuler/contents/pe001-multiple-of-3-and-5.py?ref=master\",\"git\":\"https://api.github.com/repos/ghostdsb/ProjectEuler/git/blobs/8f42d5105610d2625069cea1605ec833b0ba279a\",\"html\":\"https://github.com/ghostdsb/ProjectEuler/blob/master/pe001-multiple-of-3-and-5.py\"}}",
   headers: [
     {"content-type", "application/json; charset=utf-8"},
     {"status", "200 OK"},
     {"last-modified", "Thu, 02 Nov 2017 09:53:25 GMT"},
     ...
   ],   
   status_code: 200,
   ...
 }}
```

The body is in json format so we use ```Jason```  to decode, and then again the contents are encoded so we decode the contents by ```Base.decode64!/1```

```elixir
def get_answer_data(file_name) do
    with {:ok, %HTTPoison.Response{status_code: 200, body: body, headers: headers}} <- HTTPoison.get("https://api.github.com/repos/ghostdsb/ProjectEuler/contents/"<>file_name<>"?ref=master"),
      {:ok, data} <- body |> Jason.decode() do
      answer_text =
        data["content"]
        |> String.split("\n")
        |> Enum.map(fn line -> line |> Base.decode64!() end)
        |> Enum.join()
      %{
        "body" => answer_text,
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
```elixir
iex(8)> ExScapper.get_answer_data("pe001-multiple-of-3-and-5.py", :timed)
%{
  "body" => "#pe001\r\narr = [x for x in range(1,1000) if x%3==0 or x%5==0]\r\nprint(sum(arr))\r\n",
  "headers" => %{
    "last-modified" => "Thu, 02 Nov 2017 09:53:25 GMT",
  }
}
```
Great, we got the body that looks like a python code. So we are done with building the answer.

Now time to fetch the questions.

#### Scraping questions from Project Euler site
---

Same HTTPoison module is used to fetch the site details. But now another elixir module Floki which is a simple HTML parser that enables search for nodes using CSS selectors. Upon inspecting the site, it is found that the question title is wrapped in an ```h2``` tag and the question content is inside a ```div``` with class ```problem_content```.

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

The only issue is Floki returns HTML data as a tuple of ```{tag_name, attributes, children_nodes_list}```

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

```htmlfy/1```converts the Floki data to a valid HTML.

```elixir
# for self closing tags
def htmlfy({tag_name, _attributes, []}) do
    "<#{tag_name}/>"
end

# recursively htmlfy-ies the children
def htmlfy({tag_name, _attributes, children_nodes}) do
    "<#{tag_name}>#{Enum.reduce(children_nodes,"",fn child, acc -> acc <> htmlfy(child) end )}</#{tag_name}>"
end

# returns a string child as it is
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

[ExScaper's repo](https://github.com/ghostdsb/ex_scapper)