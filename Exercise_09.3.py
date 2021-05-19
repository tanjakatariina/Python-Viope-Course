def main():
    while True:
        syote = input("Anna syöte (Lopeta lopettaa): ")
        if syote == "Lopeta":
            break
        elif len(syote) >= 5:
            tulostaja(syote)
        else:
            tulostaja()


def tulostaja(tulostus="Oletustulostus"):
    print(tulostus)


if __name__ == "__main__":
    main()
