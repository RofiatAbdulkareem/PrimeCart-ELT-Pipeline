resource "aws_s3_bucket" "elt-bucket" {
  bucket = "aws-elt-bucket"

  tags = {
    Name        = "My bucket"
    Environment = "Production"
    Team = "Data Engineering Team"
    Managed_by = "Terraform"
  }
}