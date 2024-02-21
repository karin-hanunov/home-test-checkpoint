
module "lambda_function" {
  source = "./modules/github_function"
}

module "api_gateway" {
  source = "./modules/api_gateway"
  api_gateway_region = var.region
  lambda_function_name = module.lambda_function.lambda_function_name
  lambda_function_arn = module.lambda_function.lambda_function_arn
  depends_on = [
    module.lambda_function
  ]
}

