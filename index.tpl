<html>

  <head>
    <title>TODO List</title>
  </head>

  <body>

    <a href="new">New</a> <br />

    <p>The open items are as follows:</p>

    <table border="1">
    %for row in rows:
    <tr>

        <td>{{row[0]}}</td>
        <td><a href="edit/{{row[0]}}">{{row[1]}}</a></td>

    </tr>
    %end
    </table>

  </body>
</html>
