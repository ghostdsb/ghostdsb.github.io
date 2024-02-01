---
layout: post
title:  "RayTracer"
date:   2021-03-14 11:48:13 +0530
category: Project
permalink: "projects/raytracer"
tags: ["Rust", "Math", "Physics"]
---

# Raytracer in Rust


```rust

fn make_image()->String{

    // empty ppm image
    let mut image = String::new();
    
    // image dimensions
    let width:u32 = constants::WIDTH as u32;
    let height:u32 = constants::HEIGHT as u32;

    // camera distance
    let focal = Vec3::new(0.0, 0.0, constants::FOCAL_LENGTH);

    // setting up camera
    let camera = Camera::camera();

    // initializing world
    let mut world = HittableList::new();
    
    // adding 2 spheres to world
    let sphere = Sphere::new(-focal, 0.5);
    let sphere2 = Sphere::new(Vec3::new(0.0, -100.5, -1.0), 100.0);
    world.add(Box::new(sphere2));
    world.add(Box::new(sphere));

    image.push_str(&format!("P3\n{} {}\n255\n",width, height));
    
    // image creator
    for y in (0..height).rev(){
        for x in 0..width{

            let u:f32 = (x as f32) / width as f32;
            let v:f32 = (y as f32) / height as f32;

            // starting a ray from camera to image plane
            let ray: Ray = camera.get_ray(u, v);

            // calculating the color of pixel where ray hits image plane
            let pixel_color = ray_color(&ray, &world, constants::MAX_DEPTH);

            // writing pixel value to image
            write_color(&mut image, &pixel_color);
        }
    }
    image
}

```


1. ## hello world
---
![hello_world](../assets/output/1_hello_world.png)

2. ## blue lerp
---
![blue lerp](../assets/output/2_blue_lerp.png)

3. ## hit_sphere
---
![3_hit_sphere](../assets/output/3_hit_sphere.png)

4. ## hit_sphere_surface_normals
---
![4_hit_sphere_surface_normals](../assets/output/4_hit_sphere_surface_normals.png)

5. ## hittable_lists
---
![6_hittable_lists](../assets/output/6_hittable_lists.png)

6. ## diffuse_material
---
![9_diffuse_material](../assets/output/9_diffuse_material.png)

7. ## shadow_acne
---
![9a_shadow_acne](../assets/output/9a_shadow_acne.png)

8. ## lambertian_reflection
---
![9b_lambertian_reflection](../assets/output/9b_lambertian_reflection.png)

9. ## corrected_lambertian_reflection
---
![9c_corrected_lambertian_reflection](../assets/output/9c_corrected_lambertian_reflection.png)
