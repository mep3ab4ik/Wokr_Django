from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
# Create your models here.


class FriendList(models.Model):
    # Одному пользователю - один список друзей
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_friendlist')
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='friends')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    # Второй параметр, кого мы хотим добавить
    def add_friend(self, account):
        """
        Add a new friend
        """

        if not account in self.friends.all():
            self.friends.add(account)
            self.save()

    def remove_friend(self, account):
        """
        Remove a friend
        """

        if account in self.friends.all():
            self.friends.remove(account)
            self.save()

    def unfriend(self, removee):
        """
        Initiate the action of unfriending someone
        """
        remove_friend_list = self  # person terminating the friendship

        # remove friend from remover friend list
        remove_friend_list.remove_friend(removee)

        # remove friend from removee friend list
        friend_list = FriendList.objects.get(user=removee)
        friend_list.remove_friend(self.user)


    def in_mutual_friend(self, friend):
        """
        It is friend?
        """
        if friend in self.friends.all():
            return True
        return False


class FriendRequest(models.Model):
    """
    A friend request consists of two main parts:
        1. SENDER
            - Person sending/initiating the friend request
        2. RECEIVER
            - Person receiving the friend request
    """

    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver')
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestapm = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    def accept(self):
        """
        Accept a friend request
        Update both SENDER and RECEIVER friend list
        """
        receiver_friend_list = FriendList.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False
                self.save()

    def decline(self):
        """
        Decline a friend request.
        It is 'declined' by settings the 'is_active' field to False
        """
        self.is_active = False
        self.save()

    def cancel(self):
        """
        Cancel a friend request.
        It is 'cancelled' by settings the 'is_active' field to False.
        This is only different with respect to 'declining' through the notification that is generated.
        """
        self.is_active = False
        self.save()


class SubscribeList(models.Model):
    # Одному пользователю - один список подписок
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_subscribelist')
    sub = models.ManyToManyField(User, blank=True, related_name='subscribe')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username