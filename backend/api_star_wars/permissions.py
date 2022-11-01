from rest_framework import permissions

class IsCustomerPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        #Permissions for Planets
        if user.has_perm("api_star_wars.create_planets"):
            return True
        if user.has_perm("api_star_wars.list_planets"):
            return True
        if user.has_perm("api_star_wars.update_planets"):
            return True
        if user.has_perm("api_star_wars.delete_planets"):
            return True
        if user.has_perm("api_star_wars.search_planets"):
            return True
        if user.has_perm("api_star_wars.detail_planets"):
            return True
        #Permissions for Directors
        if user.has_perm("api_star_wars.create_director"):
            return True
        if user.has_perm("api_star_wars.list_director"):
            return True
        if user.has_perm("api_star_wars.update_director"):
            return True
        if user.has_perm("api_star_wars.delete_director"):
            return True
        if user.has_perm("api_star_wars.search_director"):
            return True
        if user.has_perm("api_star_wars.detail_director"):
            return True
        #Permissions for Productors
        if user.has_perm("api_star_wars.create_productors"):
            return True
        if user.has_perm("api_star_wars.list_productors"):
            return True
        if user.has_perm("api_star_wars.update_productors"):
            return True
        if user.has_perm("api_star_wars.delete_productors"):
            return True
        if user.has_perm("api_star_wars.search_productors"):
            return True
        if user.has_perm("api_star_wars.detail_productors"):
            return True
        #Permissions for Movies
        if user.has_perm("api_star_wars.create_movies"):
            return True
        if user.has_perm("api_star_wars.list_movies"):
            return True
        if user.has_perm("api_star_wars.update_movies"):
            return True
        if user.has_perm("api_star_wars.delete_movies"):
            return True
        if user.has_perm("api_star_wars.search_movies"):
            return True
        if user.has_perm("api_star_wars.detail_movies"):
            return True
        #Permissions for Character
        if user.has_perm("api_star_wars.create_characters"):
            return True
        if user.has_perm("api_star_wars.list_characters"):
            return True
        if user.has_perm("api_star_wars.update_characters"):
            return True
        if user.has_perm("api_star_wars.delete_characters"):
            return True
        if user.has_perm("api_star_wars.search_characters"):
            return True
        if user.has_perm("api_star_wars.detail_characters"):
            return True
        return False
