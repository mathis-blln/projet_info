from view.start_view import StartView


def main():
    start_view = StartView()
    user_choice = start_view.make_choice()

    if user_choice is None:
        print("Aucune action sélectionnée.")
    else:
        print(f"L'option sélectionnée est {type(user_choice).__name__}.")


if __name__ == "__main__":
    main()
