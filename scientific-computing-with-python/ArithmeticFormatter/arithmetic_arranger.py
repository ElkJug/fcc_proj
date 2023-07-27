# Arithmetic arranger: map data, then check input, last draw out data
def arithmetic_arranger(problems: 'list' = [], format: bool = False) -> str():
    maped = map(problems)
    errormsg = checkinput(maped)
    if errormsg != '': return f'Error: {errormsg}'
    return draw(maped, format)


def checkinput(mapedprob):  # check and see if input is according to constrant

    if len(mapedprob) > 5: return 'Too many problems.'
    for problem in mapedprob:
        print(problem)
        if problem['opt'] not in ['+', '-']:
            return "Operator must be '+' or '-'."
        if not (problem['top'].isdigit() and problem['bot'].isdigit()):
            return 'Numbers must only contain digits.'
        if not (len(problem['top']) <= 4 and len(problem['bot']) <= 4):
            return 'Numbers cannot be more than four digits.'
    return ''


def map(problems) -> list():  # map data
    map = list()
    for problem in problems:
        eachmap = problem.split(' ')
        top = eachmap[0]
        bot = eachmap[2]
        opt = eachmap[1]
        thismap = {'top': top, 'bot': bot, 'opt': opt}
        map.append(thismap)
    return map


def draw(mapped, out_toggle):
    drawstr = ['', '', '']
    if out_toggle: drawstr.append('')

    for i, m in enumerate(mapped):
        # calculate output
        top = m['top']
        bot = m['bot']
        opt = m['opt']
        # calculate best fit width
        w = len(top) if len(top) > len(bot) else len(bot)
        # draw formatter
        drawstr[0] += top.rjust(w + 2)
        drawstr[1] += opt + ' ' + bot.rjust(w)
        drawstr[2] += '-' * (w + 2)
        # draw output
        if out_toggle:
            out = int(top) + int(bot) if opt == '+' else int(top) - int(bot)
            out = str(out)
            drawstr[3] += out.rjust(w + 2)
        # draw seperater but not the last
        if i < len(mapped) - 1:
            for i, line in enumerate(drawstr):
                drawstr[i] += 4 * ' '

    # finish formatting drawing, draw parts
    drawstr = '\n'.join(drawstr)
    return drawstr
