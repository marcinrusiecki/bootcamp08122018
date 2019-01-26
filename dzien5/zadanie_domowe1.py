def sumator(args):
    if isinstance(args, dict):
        args = args.values()
    total = 0
    for x in args:
        try:
            x = int(x)
            total +=x
        except ValueError:
            pass
    return total

print(sumator({"sum":1,"sum2":2}))
