resource "aws_s3_bucket" "example" {
  bucket = "my-tf-test-bucket"
  bucket_prefix = "stg"
  force_destroy = True

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}