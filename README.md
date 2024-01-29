Код не смотреть, можно только после успешного запуска
<form action="/Store" method="post" class="form_flex">
  <h3>Создать банан</h3>
  <div class="form_input-box">
    <input type="text" name="name" placeholder="Введите название"/>
    <span style="color: red"><?=!empty($errors) && isset($errors['name']) ? $errors['name'] : '' ?></span>
  </div>
  <div class="form_input-box">
    <input type="text" name="price"  placeholder="Введите цену"/>
    <span style="color: red"><?=!empty($errors) && isset($errors['price']) ? $errors['price'] : '' ?></span>
  </div>
  <div class="form_input-box">
    <input type="text" name="preview"  placeholder="Введите ссылку на картинку"/>
    <span style="color: red"><?=!empty($errors) && isset($errors['preview']) ? $errors['preview'] : '' ?></span>
  </div>
  <button class="form_button" id="closeFormButton" type="submit">Отправить</button>
</form>