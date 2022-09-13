def arithmetic_arranger(problems, *display):
  show = False
  for check in display:
    show = check
  if len(problems) > 5:
    return "Error: Too many problems."
  else:
    data = [i.split() for i in problems]
  for i in data:
    try:
      int(i[0]), int(i[2])
    except:
      return "Error: Numbers must only contain digits."
    if not(i[1] in ["+", "-"]):
      return "Error: Operator must be '+' or '-'."
    elif(i[1] == "+"):
      i.append((len(sorted(i, key=len)[-1])+2) * "-")
      i.append(str(int(i[0])+int(i[2])))
    elif(i[1] == "-"):
      i.append((len(sorted(i, key=len)[-1])+2) * "-")
      i.append(str(int(i[0])-int(i[2])))
    if (len(i[0])>4 or len(i[2])>4):
      return "Error: Numbers cannot be more than four digits."
  unarranged_problems = ["", "", "", ""]
  for i in data:
    columns = len(i[3])
    i[0] = " " * (columns - len(i[0])) + i[0]
    i[2] = i[1] + " " * (columns - len(i[2]) - 1) + i[2]
    i[4] = " " * (columns - len(i[4])) + i[4]
    unarranged_problems[0] = unarranged_problems[0] + i[0] + "    "
    unarranged_problems[1] = unarranged_problems[1] + i[2] + "    "
    unarranged_problems[2] = unarranged_problems[2] + i[3] + "    "
    unarranged_problems[3] = unarranged_problems[3] + i[4] + "    "
  unarranged_problems = [i.rstrip() for i in unarranged_problems]
  if show:
    arranged_problems = "\n".join(unarranged_problems)
  else:
    arranged_problems = "\n".join(unarranged_problems[:-1])
  return arranged_problems