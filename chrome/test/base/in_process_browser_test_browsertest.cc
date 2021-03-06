// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include <string.h>

#include "chrome/browser/ui/browser.h"
#include "chrome/browser/ui/tabs/tab_strip_model.h"
#include "chrome/test/base/in_process_browser_test.h"
#include "chrome/test/base/ui_test_utils.h"
#include "content/public/browser/render_view_host.h"
#include "content/public/browser/web_contents.h"
#include "content/public/browser/web_contents_observer.h"
#include "net/base/net_errors.h"
#include "testing/gtest/include/gtest/gtest.h"

namespace {

class InProcessBrowserTestP
    : public InProcessBrowserTest,
      public ::testing::WithParamInterface<const char*> {
};

IN_PROC_BROWSER_TEST_P(InProcessBrowserTestP, TestP) {
  EXPECT_EQ(0, strcmp("foo", GetParam()));
}

INSTANTIATE_TEST_CASE_P(IPBTP,
                        InProcessBrowserTestP,
                        ::testing::Values("foo"));

// WebContents observer that can detect provisional load failures.
class LoadFailObserver : public content::WebContentsObserver {
 public:
  explicit LoadFailObserver(content::WebContents* contents)
      : content::WebContentsObserver(contents),
        failed_load_(false),
        error_code_(net::OK) { }

  virtual void DidFailProvisionalLoad(
      int64 frame_id,
      const base::string16& frame_unique_name,
      bool is_main_frame,
      const GURL& validated_url,
      int error_code,
      const base::string16& error_description,
      content::RenderViewHost* render_view_host) OVERRIDE {
    failed_load_ = true;
    error_code_ = static_cast<net::Error>(error_code);
    validated_url_ = validated_url;
  }

  bool failed_load() const { return failed_load_; }
  net::Error error_code() const { return error_code_; }
  const GURL& validated_url() const { return validated_url_; }

 private:
  bool failed_load_;
  net::Error error_code_;
  GURL validated_url_;

  DISALLOW_COPY_AND_ASSIGN(LoadFailObserver);
};

// Tests that InProcessBrowserTest cannot resolve external host, in this case
// "google.com" and "cnn.com". Using external resources is disabled by default
// in InProcessBrowserTest because it causes flakiness.
IN_PROC_BROWSER_TEST_F(InProcessBrowserTest, ExternalConnectionFail) {
  content::WebContents* contents =
      browser()->tab_strip_model()->GetActiveWebContents();

  const char* const kURLs[] = {
    "http://www.google.com/",
    "http://www.cnn.com/"
  };
  for (size_t i = 0; i < arraysize(kURLs); ++i) {
    GURL url(kURLs[i]);
    LoadFailObserver observer(contents);
    ui_test_utils::NavigateToURL(browser(), url);
    EXPECT_TRUE(observer.failed_load());
    EXPECT_EQ(net::ERR_NOT_IMPLEMENTED, observer.error_code());
    EXPECT_EQ(url, observer.validated_url());
  }
}

}  // namespace
