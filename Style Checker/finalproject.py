import random
import math

def compare_dictionaries(d1, d2):
    """ compares two dictionaries and gives an overall score to a feature """
    score = 0
    if type(d1) != dict:
        d1 = dict(d1)
    if type(d2) != dict:
        d2 = dict(d2)
    g1 = num_dict(d1)
    g2 = num_dict(d2)
    for x in d2:
        if x in d1:
            t = d2[x]/g2
            s = d1[x] * math.log10(t)
            score += s
        else:
            t = 0.5/g2
            s = d2[x] * math.log10(t)
    f = str(score)
    for x in range(len(f)):
        if f[x] == '.':
            g = x
    g += 4
    f = f[:g]
    f = float(f)
    return f
    
def num_dict(listx):
    """ returns the sum of all the values in a dictionary. """
    a = list(listx.values())
    g = sum(a)
    return g

def max_index(listx):
    """ returns the index of the highest value in a list. """
    for x in range(len(listx)):
        if max(listx) == listx[x]:
            return x

def maxes(listx):
    ''' arranges the values of all the word appearances in the order of
        high to low and passes that on to another function to make a
        dictionary for the best words. '''
    xyz = []
    a = list(listx.values())
    for d in range(len(a)):
        x = max(a)
        xyz += [x]
        g = max_index(a)
        a = a[0:g] + a[g+1:]
    f = get_values(listx, xyz)
    return f

def get_values(listx, dict1):
    ''' makes a dictionary for the best 100 words.
        words as keys and their appearances as values for them.'''
    listd = {}
    count = 1
    for v in dict1:
        for x in listx:
            if listx[x] == v:
                listd[x] = v
                count += 1
                if len(listd) == 100:
                    return listd
    return listd

def create_new_stem(s):
    ''' creates a list of all the stems in a document. '''
    g = [ ]
    s = clean_text(s)
    for x in s:
        x = x.lower()
        g += [stem(x)]
    return g

def stem(s):
    ''' takes a normal word as an input and turns them into a stem,
        many similar words can have the same stem '''
    if len(s) == 0:
        s = s
    elif len(s) == 2:
        s = s
    elif s[-3:] == 'ing':
        if len(s) == 4:
            s = s
        elif s[-4] == s[-5]:
            if len(s) == 6:
                s = s[:-3]
            else:
                s = s[:-4]
        else:
            s = s[:-3]
    elif s[-2:] == 'er':
        s = s[:-2]
    elif s[-3:] == 'ers':
        s = s[:-3]
    elif s[-1] == 'y':
        s = s[:-1] + 'i'
    elif s[-3:] == 'ies':
        s = s[:-3] + 'y'
    elif s[-1:] == 's':
        s = s[:-1]
    elif s[-2:] == 'ed':
        s = s[:-2]
    elif s[-1:] == 'e':
        if len(s) == 4:
            s = s[:-1]
    return s

def clean_text(txt):
    ''' cleans the text of all kinds of punctuation marks
        and other extra characters. '''
    while '.' in txt:
        txt = txt.replace('.', '')
    while ':' in txt:
        txt = txt.replace(':', '')
    while ';' in txt:
        txt = txt.replace(';', '')
    while ',' in txt:
        txt = txt.replace(',', '')
    while '?' in txt:
        txt = txt.replace('?', '')
    while '-' in txt:
        txt = txt.replace('-', '')
    while '!' in txt:
        txt = txt.replace('!', '')
    while '/n' in txt:
        txt = txt.replace('/n', '')
    while '/' in txt:
        txt = txt.replace('/', '')
    while "\'" in txt:
        txt = txt.replace('\'', '')
    while ')' in txt:
        txt = txt.replace(')', '')
    while '(' in txt:
        txt = txt.replace('(', '')
    
    txt = txt.split(' ')
    return txt

class TextModel:
    ''' A class that defines the TextModel. '''
    def __init__(self, model_name):
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.best_words = []

    def __repr__(self):
        ''' returns a string that includes the name of the model as
            well as the sizes of the dictionaries for each feature of the text. '''
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  the best words and their number of appearances: ' + str(self.best_words)
        return s

    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.
        """
        a = s.lower()
        word_list = clean_text(a)
        word_listx = clean_text(a)
        word_listg = create_new_stem(a)
        sentence_l = s.split('.')
        if len(sentence_l[-1]) == 0:
           sentence_l = sentence_l[:-1]


        for y in word_listx:
            a = len(y)
            if a in self.word_lengths: 
                self.word_lengths[a] += 1
            else:
                self.word_lengths[a] = 1

        for y in word_listx:
            if y in self.words:
                self.words[y] += 1
            else:
                self.words[y] = 1

        for r in word_listg:
            if r in self.stems:
                self.stems[r] += 1
            else:
                self.stems[r] = 1


        for u in range(len(sentence_l)):
            sentence_l[u] = sentence_l[u].split(' ')
            if sentence_l[u][0] == '':
                sentence_l[u] = sentence_l[u][1:]
            a = len(sentence_l[u])
            g = self.sentence_lengths
            if a in g:
                g[a] += 1
            else:
                g[a] = 1

        self.best_words = maxes(self.words)

    def add_file(self, filename):
        ''' adds all of the text in the file identified by filename to the model '''
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        s = f.read()
        self.add_string(s)

    def save_model(self):
        ''' saves the TextModel object self by writing its
            various feature dictionaries to files '''
        d1 = self.word_lengths
        filename1 = str(self.name) + '_word_lengths'
        f1 = open(filename1, 'w')
        f1.write(str(d1))
        f1.close()

        d2 = self.words
        filename2 = str(self.name) + '_words'
        f2 = open(filename2, 'w')
        f2.write(str(d2))
        f2.close()

        d3 = self.stems
        filename3 = str(self.name) + '_stems'
        f3 = open(filename3, 'w')
        f3.write(str(d3))
        f3.close()

        d4 = self.sentence_lengths
        filename4 = str(self.name) + '_sentence_lengths'
        f4 = open(filename4, 'w')
        f4.write(str(d4))
        f4.close()

        d5 = self.best_words
        filename5 = str(self.name) + '_best_words'
        f5 = open(filename5, 'w')
        f5.write(str(d5))
        f5.close()

    def read_model(self):
        ''' reads the stored dictionaries for the called TextModel
            object from their files and assigns them to the attributes
            of the called TextModel. '''
        filename1 = str(self.name) + '_word_lengths'
        f1 = open(filename1, 'r')    
        d1_str = f1.read()           
        f1.close()
        self.word_lengths = dict(eval(d1_str))

        filename2 = str(self.name) + '_words'
        f2 = open(filename2, 'r')    
        d2_str = f2.read()           
        f2.close()
        self.words = dict(eval(d2_str))

        filename3 = str(self.name) + '_stems'
        f3 = open(filename3, 'r')    
        d3_str = f3.read()           
        f3.close()
        self.stems = dict(eval(d3_str))

        filename4 = str(self.name) + '_sentence_lengths'
        f4 = open(filename4, 'r')    
        d4_str = f4.read()           
        f4.close()
        self.sentence_lengths = dict(eval(d4_str))

        filename5 = str(self.name) + '_best_words'
        f5 = open(filename5, 'r')    
        d5_str = f5.read()           
        f5.close()
        self.best_words = dict(eval(d5_str))

    def similarity_scores(self, other):
        ''' computes and returns a list of log similarity
            scores measuring the similarity of self and other '''
        score = []
        word_score_words = compare_dictionaries(other.words, self.words)
        word_score_word_lengths = compare_dictionaries(other.word_lengths, self.word_lengths)
        word_score_best_words = compare_dictionaries(other.best_words, self.best_words)
        word_score_stems = compare_dictionaries(other.stems, self.stems)
        word_score_sentence_lengths = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)

        score += [word_score_words]
        score += [word_score_sentence_lengths]
        score += [word_score_word_lengths]
        score += [word_score_best_words]
        score += [word_score_stems]
        return score

    def classify(self, source1, source2):
        ''' compares the called TextModel object (self) to two
            other “source” TextModel objects '''
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for', source1.name, ':', scores1)
        print('scores for', source2.name, ':', scores2)
        
        for x in range(len(scores1)):
            weighted_sum1 = 0
            weighted_sum1 += 10*scores1[x]
        for y in range(len(scores2)):
            weighted_sum2 = 0
            weighted_sum2 += 10*scores2[y]
            
        if weighted_sum1 < weighted_sum2:
            print(self.name, 'is more likely to have come from', source1.name)
        elif weighted_sum2 < weighted_sum1:
            print(self.name, 'is more likely to have come from', source2.name)
        else:
            print(source2.name, 'and', source1.name, 'are both the same as', self.name)

    
def run_tests():
    """ test runs between 2 source texts and a sample text body. """
    source1_name = str(input('Enter name of first source: '))
    source1_filename = str(input('Enter filename with extension of first source: '))
    source2_name = str(input('Enter name of second source: '))
    source2_filename = str(input('Enter filename with extension of first source: '))
    sample_name = str(input('Enter name of sample file: '))
    sample_filename = str(input('Enter filename with extension of first source: '))

    source3 = TextModel(source1_name)
    source3.add_file(source1_filename)

    source4 = TextModel(source2_name)
    source4.add_file(source2_filename)

    new2 = TextModel(sample_name)
    new2.add_file(sample_filename)
    
    new2.classify(source3, source4)
    print()


run_tests()
    
        
