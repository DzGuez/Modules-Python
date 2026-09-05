#!/usr/bin/env python3

import alchemy.transmutation as transmutation


def main() -> None:
    print("=== Transmutation 1 ===")

    print("Import transmutation module directly")
    print(
            "Testing lead to goal: "
            f"{transmutation.recipes.lead_to_gold()}\n"
    )


if __name__ == "__main__":
    main()
