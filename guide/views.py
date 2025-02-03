
from .models import GuidePost

from .forms import CommentForm,Comment
from django.shortcuts import redirect
# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormMixin

class IndexView(ListView):
    template_name='main.html'
    content_object_name='object_list'
    queryset=GuidePost.objects.order_by('-posted_at')

class GuideDetail(DetailView):

    template_name ='detail.html'
    model = GuidePost
    context_object_name='guidepost'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comments'] = Comment.objects.filter(guidepost=self.get_object())
        context['form'] = CommentForm()  # フォームをコンテキストに追加
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)  # フォームにデータをバインド
        if form.is_valid():  # フォームのバリデーションをチェック
            comment = form.save(commit=False)  # データベースに保存せずインスタンスを取得
            comment.guidepost = self.get_object()  # 関連付けるGuidePostオブジェクトを設定
            comment.save()  # データベースに保存
            return redirect('guide_detail', pk=self.get_object().pk)  # リダイレクト
        else:
            return self.render_to_response(self.get_context_data(form=form))  # フォームにエラーがあれば再描画
class FormDerailView(FormMixin,DetailView):
    model =Comment
    