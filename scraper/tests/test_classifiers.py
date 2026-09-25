"""Unit tests for src/classifiers.py."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from src.classifiers import article_categories


class TestArticleCategories:
    """Tests for the article_categories function."""

    @patch("src.classifiers._gist")
    @patch("src.classifiers._gist_lock")
    def test_returns_empty_list_for_empty_text(
        self, mock_lock: MagicMock, mock_gist: MagicMock
    ) -> None:
        """When both title and description are empty, should return empty list."""
        result = article_categories("", "")
        assert result == []
        mock_gist.classify.assert_not_called()

    @patch("src.classifiers._gist")
    @patch("src.classifiers._gist_lock")
    def test_combines_title_and_description(
        self, mock_lock: MagicMock, mock_gist: MagicMock
    ) -> None:
        """Should combine title and description into text for classification."""
        mock_topic_1 = MagicMock()
        mock_topic_1.name = "sports"
        mock_topic_2 = MagicMock()
        mock_topic_2.name = "technology"
        mock_gist.classify.return_value = [mock_topic_1, mock_topic_2]

        result = article_categories("Tech News", "Breaking technology update")
        assert result == ["sports", "technology"]
        mock_gist.classify.assert_called_once()
        args, kwargs = mock_gist.classify.call_args
        assert "Tech News" in args[0]
        assert "Breaking technology update" in args[0]
        assert kwargs["top_k"] is not None

    @patch("src.classifiers._gist")
    @patch("src.classifiers._gist_lock")
    def test_skips_empty_parts_when_building_text(
        self, mock_lock: MagicMock, mock_gist: MagicMock
    ) -> None:
        """Should only include non-empty parts when building the classification text."""
        mock_topic = MagicMock()
        mock_topic.name = "news"
        mock_gist.classify.return_value = [mock_topic]

        article_categories("Only Title", "")
        mock_gist.classify.assert_called_once()
        text = mock_gist.classify.call_args[0][0]
        assert text == "Only Title"

    @patch("src.classifiers._gist")
    @patch("src.classifiers._gist_lock")
    def test_strips_parts_before_classification(
        self, mock_lock: MagicMock, mock_gist: MagicMock
    ) -> None:
        """Should strip whitespace from title and description parts."""
        mock_gist.classify.return_value = []

        article_categories("  Spaced Title  ", "  Spaced Description  ")
        text = mock_gist.classify.call_args[0][0]
        assert "  Spaced Title  " not in text
        assert "Spaced Title" in text
        assert "Spaced Description" in text

    @patch("src.classifiers._gist")
    @patch("src.classifiers._gist_lock")
    def test_returns_empty_when_no_topics(
        self, mock_lock: MagicMock, mock_gist: MagicMock
    ) -> None:
        """Should return empty list when classify returns no topics."""
        mock_gist.classify.return_value = []

        result = article_categories("Some Title", "Some Description")
        assert result == []
