provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

data "template_file" "user_data" {
  template = "${file("setup.sh")}"
}

resource "aws_instance" "command-center" {
  count                       = 1
  ami                         = "ami-062f7200baf2fa504"
  instance_type               = "t3a.nano"
  key_name                    = "${aws_key_pair.command_center.key_name}"
  associate_public_ip_address = true
  user_data                   = "${data.template_file.user_data.rendered}"

  iam_instance_profile = "iam-role-command-center"

  tags = {
    Name = "Command Center"
  }
}

resource "aws_key_pair" "command_center" {
  key_name   = "command_center"
  public_key = "${file("command_center.pub")}"
}

resource "aws_s3_bucket" "credentials" {
  bucket  = "rb-int-us-east-1-bot-credentials"
  acl     = "private"

  tags = {
    Name  = "Bot Credential Storage"
  }
}
