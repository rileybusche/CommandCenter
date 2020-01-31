output "ip" {
  value = aws_instance.command-center[0].public_ip
}