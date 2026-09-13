
import json
import mysql.connector
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .signup import signup
from .login import login 
from .cases import cases
from  .abuser import abuser
from  .victim import victim

from datetime import date


@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Email = data.get("Email")
        Full_name = data.get("Full_name")
        Create_password = data.get("Create_password")
        Gender = data.get("Gender")

        try:
            signup(Email, Full_name, "client", Create_password, Gender)
            return JsonResponse({"message": "Signup successful"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "invalid method"}, status=405)


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Email = data.get("Email")
        Password = data.get("Password")

        try:
            result = login(Email, Password)

            if result["status"] == "no_email":
                return JsonResponse({"error": "This email is not registered"}, status=404)
            elif result["status"] == "wrong_password":
                return JsonResponse({"error": "Incorrect password"}, status=401)
            else:
                request.session["userId"] = result["userId"]
                request.session["usergroup"] = result["usergroup"]
                return JsonResponse({
                    "message": "Login successful",
                    "userId": result["userId"],
                    "fullname": result["fullname"],
                    "usergroup": result["usergroup"],
                    "gender": result["gender"]
                })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


    return JsonResponse({"error": "invalid method"}, status=405)


@csrf_exempt
def reporting_view(request):
    if request.method =="POST":
       
        data = json.loads(request.body)
        userId=data.get("userId")
        Reporter=data.get("reporter")
        Relationship=data.get("relationship")
        VictimName=data.get("victimName")
        VictimLocation=data.get("victimLocation")
        Witness=data.get("victimWitness")
        AbuseType=data.get("abusetype")
        Description=data.get("description")
        AbuserName=data.get("abuserName")

        datereported = date.today().isoformat()  
        action = "pending"


        try:
            cases(
                userId,
                Description,        # casedescription
                datereported,
                AbuserName,          # abuser
                Witness,
                VictimLocation,      # location
                VictimName,          # victim
                AbuseType,           # abuse
                action,
                Reporter,
                Relationship
            )
            return JsonResponse({"message": "Submission successful"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "invalid method"}, status=405)


@csrf_exempt
def abuser_view(request):
    if request.method== "POST":

     data = json.loads("request.body")
     AbuserName = ("abuserName")
     AbuserAge = data.get("abuserAge")
     AbuserNationalId = data.get("abuserId")
     AbuserLocation = data.get("abuserLocation")

     try:
         abuser(
             AbuserNationalId,
             AbuserName,
             AbuserAge,
             AbuserLocation,
         )
     except Exception as e:
              return JsonResponse ({"error": str(e)}, status=500)
     return JsonResponse({"error": "invalid method"}, status=405)

    @csrf_exempt
    def victim_view(request):
     if request.method== "POST":

      data = json.loads("request.body")
      VictimName = ("abuserName")
      VictimAge = data.get("abuserAge")
      VictimNationalId = data.get("abuserId")
      VictimLocation = data.get("abuserLocation")

     try:
         victim(
             VictimNationalId,
             VictimName,
             VictimAge,
                VictimLocation,
         )

      except Exception as e:
             return JsonResponse ({"error": str(e)}, status=500)
              return JsonResponse({"error": "invalid method"}, status=405)
         

                     
        
                
                
