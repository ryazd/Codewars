# https://www.codewars.com//kata/5a959662373c2e761d000183

def ticker(text, width, tick):
    tick = tick if tick < len(text) + width else tick % (len(text) + width)
    text = " " * width + text + " " * width
    return text[tick: tick + width]
