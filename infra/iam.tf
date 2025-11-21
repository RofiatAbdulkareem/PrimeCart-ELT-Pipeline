resource "aws_iam_user" "elt-user" {
  name = "elt-user"

  tags = {
    tag-key = "tag-value"
  }
}

resource "aws_iam_user_policy" "elt-user-policy" {
  name = "elt-user-policy"
  user = aws_iam_user.elt-user.name

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "*",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
