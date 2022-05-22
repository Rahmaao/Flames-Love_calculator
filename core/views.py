from django.shortcuts import render, get_object_or_404

# Create your views here.

# dict_of_answers = { 
#     0: ['Secret Admirers', "Ouuu! Looks like two shy ones might have a secret crush on each other! Been receiving notes lately? Any cards or chocolates? Who sent you those flowers - You just might have a secret admirer? 
# #     1: ['Friends', f"I really hope that you didn't have your hopes up on this one and I hate to be the one to tell ya but {name1} and {name2} are nothing more than friends at heart. Here's a tip though, try putting in some more work if you want {name2} to see you in a different way!"],
#     2: ['Lovers', "Are you testing the waters or do you really just want to see if you and your lover are truly lovers? Well, my prediction says that  I really hope that you didn't have your hopes up on this one and I hate to be the one to tell ya but you and Matt are nothing more than friends at heart. Here's a tip though, try putting in some more work if you want Matt to see you in a different way!"],
#     3: ['Admirers', "I really hope that you didn't have your hopes up on this one and I hate to be the one to tell ya but you and Matt are nothing more than friends at heart. Here's a tip though, try putting in some more work if you want Matt to see you in a different way!"],
#     4: ['Married', "I really hope that you didn't have your hopes up on this one and I hate to be the one to tell ya but you and Matt are nothing more than friends at heart. Here's a tip though, try putting in some more work if you want Matt to see you in a different way!"],
#     5: ['Enemies', "I really hope that you didn't have your hopes up on this one and I hate to be the one to tell ya but you and Matt are nothing more than friends at heart. Here's a tip though, try putting in some more work if you want Matt to see you in a different way!"],
#     }




def flames(request):
    if request.method == "POST":
        name1 = request.POST['name1']
        name2 = request.POST['name2']
        ans = algorithm(name1, name2)
        title = ans[0]
        narration = ans[1]
        context = {'result': title, 'narration': narration, 'name1': name1, 'name2':name2}
        return render(request, 'result.html', context)
        # print(ans)

    # context = {'result': ans}
    return render(request, 'index.html')
    


def algorithm(name1, name2):
    dict_of_answers = { 
    0: ['Secret Admirers', f"Ouuu! Looks like {name1} and {name2} are two shy ones and might have a secret crush on each other! Been receiving notes lately? Any cards or chocolates? Who sent you those flowers - You just might have a secret admirer! "], 
    1: ['Friends', f"I really hope that you didn't have your hopes up on this one and I hate to be the one to tell ya but {name1} and {name2} are nothing more than friends at heart. Here's a tip though, try putting in some more work if you want {name2} to see you in a different way!"],
    2: ['Lovers', f"Are you testing the waters or do you really just want to see if you and your lover are truly lovers? Well, my prediction says that {name1} and {name2} are lovers and should be in a relationship, if they aren't already in one! ;D"],
    3: ['Admirers', f"It seems that {name1} and {name2} are admirers and everyone can kinda notice it. Here's an advice, why don't you both quit beating about the bush and confess your feelings for one another? That's something you could try!"],
    4: ['Married', f"Haha! Two lil lovebirds sitting in a tree... - We all know how that rhyme ends! It would seem that {name1} and {name2} have a love so strong, they've decided to get married, or, are bound to get married! How so exciting!"],
    5: ['Enemies', f"Oh dear! I hope neither of you has a crush on the other because apparently, {name1} and {name2} hate each other's guts. However, fate does change things in the most unexpected ways, so if you're hopeful for a change in status, you just might get it xx! "],
    }
    list1 = list(name1)
    list2 = list(name2)
    x = list1[:]
    y = list2[:]
    unique = []

    for i in list1[:]:
        if not i in y:
            unique.append(i)
        else:
            y.remove(i)

    for i in list2[:]:
        if not i in x:
            unique.append(i)
        else:
            x.remove(i)

    count = len(unique)
    n = (count%6)



    return ( dict_of_answers[n] )



    