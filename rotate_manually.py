import sg90


PIN = 18

def main():
    SG90 = sg90.SG90(18)
    SG90.start()

    while True:
        try:
            deg = int(input("Set to:"))
            print(deg)
            if not (deg <= 180 and deg >= 0):
                raise Exception
        except Exception:
            print("Please enter between 0-180.")
            continue

        SG90.setDeg(deg)
    
    SG90.cleanup()


if __name__ == "__main__":
    main()