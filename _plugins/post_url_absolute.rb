module Jekyll
  class PostUrlAbsolute < Jekyll::Tags::PostUrl

    def initialize(tag_name, text, tokens)
      super
      @text = text
    end

    # Returns absolute url to a post
    def render(context)
      absolute_url("#{ super(context) }")
    end
  end
end

Liquid::Template.register_tag('post_url_absolute', Jekyll::PostUrlAbsolute)
