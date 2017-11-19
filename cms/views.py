from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from cms.forms import BookForm
from cms.models import Book


def book_list(request):
    """書籍の一覧"""
    # return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('id')
    return render(request,
                  'cms/book_list.html',  # 使用するテンプレート
                  {'books': books})        # テンプレートに渡すデータ


def book_edit(request, book_id=None):
    """書籍の編集"""
    # return HttpResponse('書籍の編集')
    if book_id: # book_idが指定されているとき（修正時）
        book = get_object_or_404() # get_object_or_404はDjangoが用意してくれるクラス
    else: # 追加時
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book) #postされたrequestデータからフォームを作成
        if form.is_valid(): # is_validはDjangoが勝手に生成していた
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list')
    else:
        form = BookForm(instance=book) # bookインスタンスからフォームを作成

    return render(request, 'cms/book_edit.html', dict(form=form, book_id=book_id))


def book_del(request, book_id):
    """書籍の削除"""
    return HttpResponse('書籍の削除')