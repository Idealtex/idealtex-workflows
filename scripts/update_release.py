from github import Github
import os
import yaml
import hashlib
import base64

try:
    github_token = os.environ['INPUT_GITHUB_TOKEN']
    new_version = os.environ['INPUT_NEW_VERSION']
    service_name = os.environ['INPUT_SERVICE_NAME']
except KeyError as e:
    print(e + " should be defined")

github = Github(github_token)


result = github.get_repo("dkalchenko/idealtex-releases").get_contents("releases.yaml")

try:
    release_content = yaml.safe_load(base64.b64decode(result.content))
except yaml.YAMLError as exc:
    print(exc)

try:
    release_content[service_name]["dev"] = new_version
except KeyError as e:
    print(e + " is not defined in release")

try:
    encode_file = yaml.safe_dump(release_content).encode('ascii')
except yaml.YAMLError as exc:
    print(exc)

github.get_repo("dkalchenko/idealtex-releases").update_file("releases.yaml", "update " + service_name + " to " + new_version, encode_file, result.sha, "main")
