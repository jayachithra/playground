from meeseeksai.meeseeksai import main


def test_meeseeksai_main(capsys):
    args = ["America/Argentina/San_Juan"]
    main()
    captured = capsys.readouterr()
    result = captured.out
    assert "San Juan!" in result