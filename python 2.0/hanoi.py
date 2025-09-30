def hanoi(n,source,destination,axelery):
    if n==0:
        return
    hanoi(n-1,source,axelery,destination)
    print(f"{n} iS moved form {source} to {destination}")
    hanoi(n-1,axelery,destination ,source)

n=int(input("enter the number : "))
hanoi(n,'A','B','C')
