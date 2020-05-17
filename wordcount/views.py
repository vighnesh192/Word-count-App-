from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    #Get every individual word
    wordlist = fulltext.split()

    #Counting each word
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #Increment the count
            worddictionary[word] += 1
        else:
            #Add to the dictionary
            worddictionary[word] = 1

    sortedDictionary = sorted(worddictionary.items(), key= operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', { 'fulltext': fulltext, 'count': len(wordlist), 'worddictionary': sortedDictionary })