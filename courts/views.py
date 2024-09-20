from django.shortcuts import get_object_or_404, redirect, render

from courts.models import Court
from members.models import Member
# def courts(request):
#     courts = Court.objects.all()
#     persons = Member.objects.all()  # Fetch all members
#     return render(request, 'all_courts.html', {'courts': courts, 'persons': persons})
def courts(request):
   courts = Court.objects.all()
   persons = Member.objects.all()
   context = {
     'courts': courts,
     'persons': persons
   }
   return render(request, "all_courts.html", context)

def release(request, id):
    court = get_object_or_404(Court, id=id)
    court.is_occupied = False
    court.save()

    # Release all members associated with this court
    members = court.members.all()
    for member in members:
        member.court = None
        member.save()
    
    return redirect('/courts/')

def reserve(request, id):
    court = get_object_or_404(Court, id=id)

    if request.method == 'POST':
        # Extract member names from the POST request
        member1_id = request.POST.get('member1')
        member2_id = request.POST.get('member2')

        if member1_id and member2_id:
            try:
                # Fetch the member objects
                member1_obj = Member.objects.get(id=member1_id)
                member2_obj = Member.objects.get(id=member2_id)
                
                # Update the court and mark as occupied
                court.is_occupied = True
                court.save()

                # Assign the court to both members
                member1_obj.court = court
                member2_obj.court = court
                member1_obj.save()
                member2_obj.save()
                
                print(f"Successfully reserved for members: {member1_obj.firstname}, {member2_obj.firstname}")
                
                return redirect('/courts/')
            except Member.DoesNotExist:
                # Handle the case where one or both members don't exist
                print(f"Error: Member with IDs {member1_id} or {member2_id} not found.")
                return redirect('/courts/')
        else:
            print("Error: Both members must be selected.")
            return redirect('/courts/')

    return redirect('/courts/')
    

