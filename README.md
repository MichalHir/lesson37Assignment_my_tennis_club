# my_tennis_club_django101

https://github.com/ranerlich7/my_tennis_club_django101


Homework: connect court and person
Let a person reserve a court
So reserve function should have a 2 select boxes of people that can reserve
# member1=models.ForeignKey(Member,on_delete=models.SET_NULL,related_name='courts', null=True,blank=True)
  # member2=models.ForeignKey(Member,on_delete=models.SET_NULL,related_name='courts', null=True,blank=True)


  def reserve(request, id):
#   court = Court.objects.get(id=id)
#   court.is_occupied = True
#   court.save()
#   return redirect('/courts/')

# def unreserve(request, id):
#   court = Court.objects.get(id=id)
#   court.is_occupied = False
#   court.save()
#   return redirect('/courts/')

python -m venv venv
.\venv\Scripts\activate
Python manage.py runserver