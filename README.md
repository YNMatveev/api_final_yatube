# YATUBE_API

YATUBE_API is a REST API application that can be used by a mobile app or chatbot for POST or GET data from Yatube Site.

## Source code

Use code hosting platform [github.com](https://github.com) to receive YATUBE_API source code.

```bash
git clone https://github.com/YNMatveev/api_final_yatube.git
```

## Requirement python package

* django
* djangorestframework
* djangorestframework-simplejwt

For install use next command:
```bash
pip install -r requirements.txt
```

## Usage

* receive list of posts
```bash
method GET
http://yatube.com/api/v1/posts
```
```js
HTTP 200 OK
[
    {
        "id": 1,
        "text": "Test Post",
        "author": "Genry",
        "pub_date": "2020-12-23T23:42:04.921619Z"
    },
    {
        "id": 2,
        "text": "Test Post 2",
        "author": "Genry",
        "pub_date": "2020-12-23T23:42:28.530167Z"
    }
]
```
* create comment for post
```bash
method POST
http://yatube.com/api/v1/posts/{post.id}/comments
{
    "post": 2,
    "text": "Test comment"
}
```
```js
HTTP 201 Created
{
    "id": 1,
    "author": "Genry",
    "post": 2,
    "text": "Test Comment",
    "created": "2020-12-23T23:43:35.329195Z"
}
```
* following to other user
```bash
method POST
http://yatube.com/api/v1/follow
{
    "following": "GreatAuthor"
}
```
```js
HTTP 201 Created
{
    "id": 4,
    "user": "SuperUser",
    "following": "GreatAuthor"
}
```

## Documentation
For detailed information refer to site [https://yatube.com/redoc](https://yatube.com/redoc)

## License
[MIT](https://choosealicense.com/licenses/mit/)