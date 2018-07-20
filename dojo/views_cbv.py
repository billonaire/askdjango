from django.http import HttpResponse
from django.views.generic import View, TemplateView



class PostListView1(View):
    def get(self, request):
        name = '성운'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
            <h1>TaskCompany</h1>
            <p>{name}
            <p>시간을 드립니다
        '''
post_list1 = PostListView1.as_view()



class PostListView2(TemplateView):
        # 'CBV: 템플릿을 통해 HTML형식 응답하기'
    template_name = 'dojo/post_list2.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '성운'
        return context
post_list2 = PostListView2.as_view()
