import django_filters
from .models import Article, Comment

class ArticleFilter(django_filters.FilterSet):

	CHOICES=(
		('oldest','Oldest'),
		('newest','Newest')
		)


	ordering = django_filters.ChoiceFilter(label="Sort By :", choices=CHOICES, method='filter_by_order')

	class Meta:
		model=Article
		fields={
		'body':['icontains'],
		'title':['icontains'], 
		'category':['exact'] ,
		'author':['exact']
		}


	def filter_by_order(self,queryset,name,value):
		expression = 'date' if value == 'oldest' else '-date'
		return queryset.order_by(expression)



class CategoryArticleFilter(django_filters.FilterSet):

	CHOICES=(
		('oldest','Oldest'),
		('newest','Newest')
		)


	ordering = django_filters.ChoiceFilter(label="Sort By :", choices=CHOICES, method='filter_by_order')

	class Meta:
		model=Article
		fields={
		'body':['icontains'],
		'title':['icontains'], 		
		'author':['exact']
		}


	def filter_by_order(self,queryset,name,value):
		expression = 'date' if value == 'oldest' else '-date'
		return queryset.order_by(expression)


