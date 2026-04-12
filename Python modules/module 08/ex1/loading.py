from importlib.metadata import version, PackageNotFoundError

print("\nLOADING STATUS: Loading programs...\n")




def check_dep(mode: bool) -> bool:
    print("Checking dependencies:")
    generate = True
    if mode:
        try:
            import tomli
            with open("pyproject.toml", "rb") as file:
                data = tomli.load(file)
                for module in data["tool"]["poetry"]["dependencies"]:
                    try:
                        if module == "python":
                            continue
                        print(f"[OK] {module} {version(module)}")
                    except PackageNotFoundError:
                        print(f"[KO] {module} not installed(pip install {module})")
                        generate = False
            print()
        except ImportError:
            print("\n###  IMPORTANT  ###")
            print("\nPackage tomli not imported")
            print("The package dependecy inspection cant be done by poetry")
            print()
            print("###################\n")
            generate = False
    else:
        with open("requirements.txt") as file:
            for module in file.read().split("\n"):
                try:
                    print(f"[OK] {module} {version(module.split('==')[0])}")
                except PackageNotFoundError:
                    print(f"[KO] {module} not installed(pip install {module})")
                    generate = False
        print()
    return generate


generate = check_dep(0)


if generate:
    import numpy
    import pandas
    import matplotlib.pyplot as plt
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    rng = numpy.random.default_rng()
    matrix = pandas.DataFrame(rng.random((20, 50)))

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")

    plt.imshow(matrix)
    plt.colorbar(label='Value Intensity')
    plt.title('Heatmap of 1000 Random Data Points')
    plt.xlabel('Columns')
    plt.ylabel('Rows')

    plt.savefig('matrix_analysis.png', dpi=500)

else:
    print("Install all required packages with:\n\
pip install -r requirements.txt\n\
or\n\
poetry install")
