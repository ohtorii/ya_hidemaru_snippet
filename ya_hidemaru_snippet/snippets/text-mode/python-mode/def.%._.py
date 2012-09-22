def Main():
    head = "def %s(" % argv[1]
    body = ",".join(argv[2:])
    tail = "):\n"
    doc  = '\t"""docstring for %s"""\n' % argv[1]
    impl = "\t%|"
    print(head + body + tail + doc + impl)

Main()
