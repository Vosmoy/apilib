import argparse
import json
from libapi_dir.libapi import get_packages


def compare_packages(branches, arch):
    results = {}
    for branch in branches:
        results[branch] = get_packages(branch, arch)
    diff = {
        "only_in_1st": {name: results[branches[0]][name] for name in set(results[branches[0]]) - set(results[branches[1]])},
        "only_in_2nd": {name: results[branches[1]][name] for name in set(results[branches[1]]) - set(results[branches[0]])},
        "higher_in_1st": {name: results[branches[0]][name] for name in set(results[branches[0]]) & set(results[branches[1]]) if results[branches[0]][name]["version"] > results[branches[1]][name]["version"] or (results[branches[0]][name]["version"] == results[branches[1]][name]["version"] and results[branches[0]][name]["release"] > results[branches[1]][name]["release"])}
    }
    return diff

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare binary packages between two branches")
    parser.add_argument("branches", nargs=2, help="Branches to compare")
    parser.add_argument("--arch", default="x86_64", help="Architecture to compare (default: x86_64)")
    args = parser.parse_args()
    branches = args.branches
    arch = args.arch
    diff = compare_packages(branches, arch)
    print(json.dumps(diff, indent=4))