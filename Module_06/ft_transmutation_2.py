#!/usr/bin/env python3

import alchemy


def main() -> None:
    print("=== Transmutation 2 ===")

    print("IMport alchemy module directly")
    print(
        "Testing lead to gold: "
        f"{alchemy.transmutation.recipes.lead_to_gold()}\n"
    )


if __name__ == "__main__":
    main()
