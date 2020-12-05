from rest_framework import serializers
from .models import Game
import datetime

class GameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    fields = ('id','name', 'release_date', 'game_category')


  def validate_name(self, value):
    nome_temp = Game.objects.filter(name=value)
    
    if nome_temp:
      raise serializers.ValidationError("O jogo informado ja existe!")
    return value
