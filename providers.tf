
provider "aws" {
  region = var.region
}

#Should be injected from GH secret
provider "github" {
  token = "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"
}

