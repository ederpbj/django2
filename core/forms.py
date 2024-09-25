from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n E-mail: {email}\n Assunto: {assunto}\n Mensagem: {mensagem}'

        # instancia o objeto da classe
        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body= conteudo,
            from_email= 'contato@seudominio.com.br',
            to=['contato@zuarts.com.br','admin@zuarts.com.br' ],
            headers={'Reply-to': email}
        )
        mail.send()