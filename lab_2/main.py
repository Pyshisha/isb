from nist import tests
from constants import JAVA_SEQUENCE, CPP_SEQUENCE, CPP_RESULT, JAVA_RESULT


def main() -> None:
    tests(JAVA_SEQUENCE, JAVA_RESULT)
    tests(CPP_SEQUENCE,  CPP_RESULT)



if __name__ == "__main__":
    main()
