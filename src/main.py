import argparse
from pathlib import Path

from client import FmcClient
from models import FmcConfig, FmcCredentials
from prompts import prompt_connection, choose_policy
from exporters import export_json, export_csv
from utils import check_connectivity, sanitize_filename, extract_linked_prefilter_id


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--csv", action="store_true")
    parser.add_argument("--output-dir", default="output")
    args = parser.parse_args()

    if not args.json and not args.csv:
        args.json = True

    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)

    base, user, pwd = prompt_connection()

    check_connectivity(base, 15)

    client = FmcClient(
        FmcConfig(base_url=base),
        FmcCredentials(user, pwd),
    )

    client.login()

    policies = client.list_access_policies()
    policy = choose_policy(policies)

    policy_id = policy["id"]
    name = sanitize_filename(policy["name"])

    full_policy = client.get_access_policy(policy_id)
    rules = client.list_access_rules(policy_id)

    if args.json:
        export_json(output_dir / f"{name}_acp.json", {"rules": rules})

    if args.csv:
        export_csv(output_dir / f"{name}_acp.csv", rules)

    pre_id = extract_linked_prefilter_id(full_policy)

    if pre_id:
        pre_rules = client.list_prefilter_rules(pre_id)

        if args.json:
            export_json(output_dir / f"{name}_prefilter.json", {"rules": pre_rules})

        if args.csv:
            export_csv(output_dir / f"{name}_prefilter.csv", pre_rules)


if __name__ == "__main__":
    main()