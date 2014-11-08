def patterncount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count

def frequentwords(text,k):
    frequentpatterns = []
    maxcount = 0
    Count = range(len(text) - k + 1)
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        Count[i] = patterncount(text,pattern)
        if Count[i] > maxcount:
            maxcount = Count[i]
    for i in range(len(text) - k + 1):
        if Count[i] == maxcount:
            frequentpatterns.append(text[i : i + k])
    return list(set(frequentpatterns))

def patterntonumber(pattern):
    baselist = ["A", "C", "G", "T"]
    k = len(pattern) - 1
    number = 0
    for letter in pattern:
        number += baselist.index(letter) * 4**k
        k -= 1
    return number

def numbertopattern(number, k):
    baselist = ["A", "C", "G", "T"]
    result = ""
    pattern = ""
    while number > 0:
        result = str(number % 4) + result
        number /= 4
    if k > len(result):
        for i in range(k - len(result)):
            result = "0" + result
    for number in result:
        pattern += baselist[int(number)]
    return pattern

def computefrequences(text, k):
    frequencyarray = [0 for i in range(4**k)]
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        j = patterntonumber(pattern)
        frequencyarray[j] += 1
    return frequencyarray

def reversecomplement(pattern):
    normal_list = ["A", "C", "G", "T"]
    complement_list = ["T", "G", "C", "A"]
    output = ""
    for i in range(len(pattern)):
        output = complement_list[normal_list.index(pattern[i])] + output
    return output

def findoccurrences(pattern, genome):
    output = ""
    for i in range(len(genome)-len(pattern)):
        if pattern == genome[i:i+len(pattern)]:
            output = output + " " + str(i)
    return output

def findclumps(genome, k, l, t):
    frequentpatterns = []
    clump = [0 for i in range(4**k)]
    for i in range(len(genome)-l):
        text = genome[i:i+l]
        frequencyarray = computefrequences(text, k)
        for j in range(4**k):
            if frequencyarray[j] >= t:
                clump[j] = 1
    for i in range(4**k):
        if clump[i] == 1:
            pattern = numbertopattern(i, k)
            frequentpatterns.append(pattern)
    return list(set(frequentpatterns))

if __name__ == "__main__":
    import sys
    input_file = open(str(sys.argv[1]),"r")
    clump_list = findclumps(str(input_file.read()).rstrip("\n"),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
    print clump_list
    print " ".join(map(str, clump_list))
#    print findclumps("CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA", 5, 50, 4)
