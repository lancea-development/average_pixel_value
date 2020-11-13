# Run project

```console
docker-compose up
```

perform a HTTP POST call like this:

```console
curl POST -F 'image=@/Users/wouterlansu/Downloads/image.jpeg' -v http://0.0.0.0:8000/images/
```

This creates an UploadedImage instance in the database which can then be use to call this url:

```console
curl GET -v http://0.0.0.0:8000/average-pixel-value/1/
```

Which will return the average pixel value of the previously created image.

The `/1/` in the url is the id of the UploadedImage so this can vary depending on how many images you've uploaded.


## Image Upload through HTTP Request

There is an endpoint to upload images into the database.

## Microservice architecture

New services can simply call this API to retrieve the image and perform their own calculations on it.

In theory the `avg_pixel_value.views.calculate_avg_pixel_value` method could run as a separate service.


## Easy integration

New image processing tasks can be easily implemented by adding methods like `avg_pixel_value.views.calculate_avg_pixel_value`.
