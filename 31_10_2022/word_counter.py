import boto3

s3_client = boto3.client("s3")

mock_event = {
    "Records": [
        {
            "s3": {
                "bucket": {"name": "example-bucket"},
                "object": {"key": "test%2Fkey", "size": 1024},
            }
        }
    ]
}


def get_bucket_name(event):
    return event["Records"][0]["s3"]["bucket"]["name"]


def get_object_name(event):
    return event["Records"][0]["s3"]["object"]["key"]


def get_object_size(event):
    return event["Records"][0]["s3"]["object"]["size"]


def count_words(string):
    words = string.split()
    # print(words)
    num_words = len(words)
    # print(num_words)
    return num_words


def lambda_handler(event, context):
    print(f"Bucket: {get_bucket_name(event)}")
    print(f"Filename: {get_object_name(event)}")
    print(f"File Size: {get_object_size(event)}")
    bucket_name = get_bucket_name(event)
    file_name = get_object_name(event)
    fixed_file_name = file_name.replace("/", "-")
    download_path = f"/tmp/{fixed_file_name}"
    s3_client.download_file(bucket_name, file_name, download_path)
    with open(download_path, encoding="utf8") as f:
        text = f.read()
        num_words = count_words(text)
        return f"The word count in the file {download_path} is {num_words}"


# if __name__ == "__main__":
#     test = count_words("this is a string")
#     print(test)
#     # count_words("This is another string with some other words")
#     with open("book.txt", encoding="utf8") as f:
#         text = f.read()
#         num_chars = len(text)
#         num_words = count_words(text)
#         print(f"The text has {num_chars} characters, and {num_words} words.")
