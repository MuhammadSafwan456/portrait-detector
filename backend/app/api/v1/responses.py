portrait = {
    "extract": {
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {"example": {"detail": "File format not supported"}}
            },
        },
        200: {
            "description": "Successful Response",
            "content": {"application/json": {"example": {"image": "base64_image"}}},
        },
    }
}
