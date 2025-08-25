from .db import SessionLocal, init_db
from .models import Problem, TestCase

init_db()

problems = [
    Problem(
        slug="reverse-array",
        title="Reverse an Array",
        difficulty="easy",
        statement_md=(
            "Given an array A of N integers, output the array in reverse order (space-separated).\n"
            "Input: N on first line; A[0..N-1] on second line."
        ),
        starter_code_py="""def reverseArray(a: list[int]) -> list[int]:
    # write your code
    return []
""",
        starter_code_java=(
            "public static java.util.List<Integer> reverseArray(java.util.List<Integer> a){
"
            "    // write your code
"
            "    return a;
"
            "}
"
        ),
        test_cases=[
            TestCase(input="4\n1 4 3 2\n", output="2 3 4 1\n", is_hidden=False),
            TestCase(input="5\n1 2 3 4 5\n", output="5 4 3 2 1\n", is_hidden=True),
        ],
    ),
    Problem(
        slug="left-rotation",
        title="Array Left Rotation",
        difficulty="easy",
        statement_md=(
            "Rotate array A left by d. Input: N d on first line; A on second. Output rotated array."
        ),
        starter_code_py="""def rotLeft(a: list[int], d: int) -> list[int]:
    # write your code
    return a
""",
        starter_code_java=(
            "public static java.util.List<Integer> rotLeft(java.util.List<Integer> a,int d){
"
            "    // write your code
"
            "    return a;
"
            "}
"
        ),
        test_cases=[
            TestCase(input="5 2\n1 2 3 4 5\n", output="3 4 5 1 2\n", is_hidden=False),
            TestCase(input="5 5\n1 2 3 4 5\n", output="1 2 3 4 5\n", is_hidden=True),
        ],
    ),
    Problem(
        slug="sparse-arrays",
        title="Sparse Arrays",
        difficulty="easy",
        statement_md=(
            "Given N strings, then Q queries, output count of each query string.\n"
            "Input: N, N lines, Q, Q lines. Output Q counts each on new line."
        ),
        starter_code_py="""def matchingStrings(strings: list[str], queries: list[str]) -> list[int]:
    # write your code
    return []
""",
        starter_code_java=(
            "public static java.util.List<Integer> matchingStrings(java.util.List<String> s, java.util.List<String> q){
"
            "    // write your code
"
            "    return java.util.List.of();
"
            "}
"
        ),
        test_cases=[
            TestCase(input="4\nab\nabc\nab\nxyz\n3\nab\nabc\nxy\n", output="2\n1\n0\n", is_hidden=False),
        ],
    ),
]

def run():
    with SessionLocal() as db:
        for p in problems:
            existing = db.query(Problem).filter_by(slug=p.slug).one_or_none()
            if existing:
                continue
            db.add(p)
        db.commit()

if __name__ == "__main__":
    run()
