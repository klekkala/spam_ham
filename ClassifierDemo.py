
from SpamClassifier import *
from copy import copy

SPAM = 'spam'
HAM = 'ham'

# change it to the type of mails you want to classify
# path to the hard ham mails


# change it to the type of mails you want to classify
# path to the hard ham mails

enron1 = 'data/enron1/'
enron2 = 'data/enron2/'
enron3 = 'data/enron3/'
enron4 = 'data/enron4/'
enron5 = 'data/enron5/'
enron6 = 'data/enron6/'

path_list = [enron1, enron2, enron3, enron4, enron5, enron6]
spam_total_paths = [s + 'spam/' for s in path_list]
ham_total_paths = [s + 'ham/' for s in path_list]

total_paths = spam_total_paths + ham_total_paths
sumer = 0
counter = 0
for j in range(len(total_paths)):

    if j < len(spam_total_paths):
        dup_spam = copy(spam_total_paths)
        test = [dup_spam[j]]
        del dup_spam[j]
        dup_ham = ham_total_paths
        print dup_spam

    else:
        dup_ham = copy(ham_total_paths)
        test = [dup_ham[j-6]]
        del dup_ham[j-6]
        dup_spam = spam_total_paths
        print dup_ham

    print test
    spam_training_set, spam_count = make_training_set(dup_spam)
    ham_training_set, ham_count = make_training_set(dup_ham)

    total_training_set = spam_training_set.copy()
    total_training_set.update(ham_training_set)
    vocabulary = len(total_training_set)

    for term in spam_training_set.keys():
        spam_training_set[term] = float((spam_training_set[term] + 1) / spam_count + vocabulary)

    for term in ham_training_set.keys():
        ham_training_set[term] = float((ham_training_set[term] + 1) / ham_count + vocabulary)


    for mail_path in test:
        mails_in_dir = [mail_file for mail_file in listdir(mail_path) if isfile(join(mail_path, mail_file))]
        counter = counter+1
        results = {}
        results[SPAM] = 0
        results[HAM] = 0
        
        print 'Running classifier on files in', mail_path[5:-1], '...'

        for mail_name in mails_in_dir:
                
            if mail_name == 'cmds':
                continue

            mail_msg = get_mail_from_file(mail_path + mail_name)
                
            # 0.2 and 0.8 because the ratio of samples for spam and ham were the same
            spam_probability = classify(mail_msg, spam_training_set, 0.5)
            ham_probability = classify(mail_msg, ham_training_set, 0.5)
                
            if spam_probability > ham_probability:
                results[SPAM] += 1
            else:
                results[HAM] += 1
                    
            total_files = results[SPAM] + results[HAM]
            spam_fraction = float(results[SPAM]) / total_files
            ham_fraction = 1 - spam_fraction
                
        print 'Individual Accuracy is '
        print max(spam_fraction, ham_fraction)

        sumer = sumer + max(spam_fraction, ham_fraction)
        

print 'Accuracy of the classifier is '
print sumer/counter

