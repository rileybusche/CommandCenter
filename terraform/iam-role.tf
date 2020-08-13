# Instance Profile
resource "aws_iam_instance_profile" "command_center" {
    name = "iam-role-command-center"
    role = "${aws_iam_role.command_center.name}"
}

# Role
resource "aws_iam_role" "command_center" {
  name = "iam-role-command-center"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF

  tags = {
    tag-key = "command center s3 access"
  }
}

# Policy
resource "aws_iam_policy" "command-center-policy" {
  name        = "command-center-policy"
  description = "Policy for Command-Center role"

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ec2:*",
            "Resource": "*"
        }

    ]
}
EOF
}

# Policy Attachment
resource "aws_iam_role_policy_attachment" "attach-command-center-role" {
  role       = "${aws_iam_role.command_center.name}"
  policy_arn = "${aws_iam_policy.command-center-policy.arn}"
}